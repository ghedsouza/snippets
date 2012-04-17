def get_dir_tree(top_level, file_pattern, include_directories = True):
    # Return a list of files matching glob_pattern by recursing through top_level
    # (like unix find command)
    dir_tree = []
    top_level_path_length = len(os.path.abspath(top_level))
    for root, dirnames, filenames in os.walk(top_level):
        if include_directories:
            for dirname in dirnames:
                dir_tree.append(os.sep + \
                    os.path.join(
                        # path relative to base_path
                        os.path.abspath(root)[top_level_path_length:], dirname))
        for filename in fnmatch.filter(filenames, file_pattern):
            dir_tree.append(
                os.path.join(
                    # path relative to base_path
                    os.path.abspath(root)[top_level_path_length:], filename))
    return dir_tree
