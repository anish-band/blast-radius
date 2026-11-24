from blast_radius.parsing import parse


def build_import_table(src_code: bytes) -> tuple[dict[str, str], list[str]]:
    res_map = {}
    res_list = []
    tree = parse(src_code)

    root_node = tree.root_node
    for child in root_node.children:
        if child.type == "import_statement":
            name_node = child.child_by_field_name("name")
            if name_node.type == "aliased_import":
                module_node = name_node.child_by_field_name("name")
                module_path = module_node.text.decode()
                alias_node = name_node.child_by_field_name("alias")
                alias_path = alias_node.text.decode()
                res_map[alias_path] = module_path

            else:
                module_path = name_node.text.decode()
                name = module_path.split(".", 1)[0]
                res_map[name] = name

    return res_map, res_list
