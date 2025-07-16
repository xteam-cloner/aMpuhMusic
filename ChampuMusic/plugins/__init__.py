import glob
import importlib
import logging
import os
import shutil
import subprocess
import sys
from os.path import abspath, dirname, isfile, join

from ChampuMusic import LOGGER

logger = LOGGER(__name__)

# Hapus pengecekan dan penghapusan folder plugin eksternal awal jika tidak lagi diperlukan.
# Jika Anda yakin folder ini tidak akan ada atau tidak perlu dihapus, bisa dilewati.
# if EXTRA_PLUGINS_FOLDER in os.listdir():
#     shutil.rmtree(EXTRA_PLUGINS_FOLDER)

# Penghapusan folder 'utils' yang mungkin terkait dengan plugin eksternal.
# Jika 'utils' sekarang selalu lokal dan tidak perlu dihapus, Anda bisa hapus baris ini.
if "utils" in os.listdir():
    shutil.rmtree("utils")

ROOT_DIR = abspath(join(dirname(__file__), "..", ".."))

# Variabel terkait plugin eksternal telah dihapus.
# external_repo_path = join(ROOT_DIR, EXTRA_PLUGINS_FOLDER)
# extra_plugins_enabled = EXTRA_PLUGINS.lower() == "False"

# Seluruh blok logika untuk mengkloning, memindahkan utilitas, dan menginstal persyaratan
# untuk plugin eksternal dihapus karena variabel-variabel terkait telah dihilangkan.
# if extra_plugins_enabled:
#     ... (seluruh blok kode ini dihapus)

def __list_all_modules():
    main_repo_plugins_dir = dirname(__file__)
    work_dirs = [main_repo_plugins_dir]

    # Logika untuk memuat extra plugins dihapus.
    # if extra_plugins_enabled:
    #     logger.info("Loading extra plugins...")
    #     work_dirs.append(join(EXTERNAL_REPO_PATH, "plugins"))

    all_modules = []

    for work_dir in work_dirs:
        mod_paths = glob.glob(join(work_dir, "*.py"))
        mod_paths += glob.glob(join(work_dir, "*/*.py"))

        modules = [
            (
                (f.replace(main_repo_plugins_dir, "ChampuMusic.plugins"))
                # Bagian ini dihapus karena tidak lagi ada EXTERNAL_REPO_PATH atau EXTRA_PLUGINS_FOLDER
                # .replace(EXTERNAL_REPO_PATH, EXTRA_PLUGINS_FOLDER)
            ).replace(os.sep, ".")[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
        ]
        all_modules.extend(modules)

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
