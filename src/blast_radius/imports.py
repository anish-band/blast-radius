from blast_radius.parsing import parse


def build_import_table(src_code: bytes) -> tuple[dict[str, str], list[str]]:
    names = {}
    star_modules = []
    tree = parse(src_code)

    root_node = tree.root_node
    for stmt_node in root_node.children:
        if stmt_node.type == "import_statement":
            name_node = stmt_node.child_by_field_name("name")
            if name_node.type == "aliased_import":
                module_node = name_node.child_by_field_name("name")
                module = module_node.text.decode()
                alias_node = name_node.child_by_field_name("alias")
                alias = alias_node.text.decode()
                names[alias] = module
            else:
                module = name_node.text.decode()
                top_level = module.split(".", 1)[0]
                names[top_level] = top_level
        elif stmt_node.type == "import_from_statement":
            module_node = stmt_node.child_by_field_name("module_name")
            module = module_node.text.decode()
            is_star = False

            for child in stmt_node.children:
                if child.type == "wildcard_import":
                    is_star = True
                    break
            if is_star:
                star_modules.append(module)
                continue

            name_node = stmt_node.child_by_field_name("name")
            if name_node.type == "aliased_import":
                symbol_node = name_node.child_by_field_name("name")
                symbol = symbol_node.text.decode()
                alias_node = name_node.child_by_field_name("alias")
                alias = alias_node.text.decode()
                names[alias] = module + "." + symbol
            else:
                symbol = name_node.text.decode()
                names[symbol] = module + "." + symbol

    return names, star_modules
