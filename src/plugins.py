# Plugin loader
#
# Modular plugin loader
import importlib

preloaded_plugins = []


def load(config):
    plugins_available = config["plugins"]

    if plugins_available:
        for plugin in plugins_available:
            plugin_key = list(plugin.keys())[0]
            plugin_data = plugin[plugin_key]
            print(f'[INFO]: {plugin_data}')
            print("[INFO] Preloading plugin: " + str(plugin_key))
            plugin_module = importlib.import_module("mods." + plugin_data["file"])
            preloaded_plugins.append((plugin_module, plugin))

        print("[INFO] Loaded plugins into memory: " + str(preloaded_plugins))
    else:
        print('[ERR] No plugins are available')


def find_plugin(command_string):
    if preloaded_plugins:
        for plugin in preloaded_plugins:
            plugin_name = list(plugin[1].keys())[0]
            print(plugin[1][plugin_name])
            if plugin[1][plugin_name]["command"] == command_string and plugin[1][plugin_name]["enabled"]:
                return plugin[0]
    else:
        print('[ERR] No pre-loaded plugins available')
