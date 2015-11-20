# Make all log messages print to stderr (useful for unit tests that hide logging)
import logging
logging.getLogger().addHandler(logging.StreamHandler())


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

def get_all_url_patterns():
    """
    Return all defined URLS in django project.
    Taken from: http://djangosnippets.org/snippets/1434/
    """
    from django.core import urlresolvers

    "Returns list of (pattern-name, pattern) tuples"
    resolver = urlresolvers.get_resolver(None)
    patterns = sorted([
        (key, value[0][0][0])
        for key, value in resolver.reverse_dict.items()
        if isinstance(key, basestring)
    ])
    return patterns
