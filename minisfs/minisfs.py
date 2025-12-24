#!/usr/bin/env python3
# Minimal FUSE filesystem (MiniFS) for NFS-Ganesha export
# Requires: python3, fuse, and `pip install fusepy`
import os, errno
from fuse import FUSE, Operations

ROOT = "/var/tmp/minifs_store"

class MiniFS(Operations):
    def _p(self, path): 
        return os.path.join(ROOT, path.lstrip("/"))

    # metadata
    def getattr(self, path, fh=None):
        p = self._p(path)
        if not os.path.exists(p):
            raise OSError(errno.ENOENT, "")
        st = os.lstat(p)
        return {
            "st_mode": st.st_mode,
            "st_nlink": st.st_nlink,
            "st_size": st.st_size,
            "st_ctime": st.st_ctime,
            "st_mtime": st.st_mtime,
            "st_atime": st.st_atime,
            "st_uid": st.st_uid,
            "st_gid": st.st_gid,
        }

    def readdir(self, path, fh):
        p = self._p(path)
        return [".", ".."] + (os.listdir(p) if os.path.isdir(p) else [])

    # file data
    def read(self, path, size, offset, fh):
        with open(self._p(path), "rb") as f:
            f.seek(offset)
            return f.read(size)

    def write(self, path, data, offset, fh):
        p = self._p(path)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "r+b" if os.path.exists(p) else "wb") as f:
            f.seek(offset)
            f.write(data)
            return len(data)

    # open/create
    def open(self, path, flags):
        return 0

    def create(self, path, mode, fi=None):
        p = self._p(path)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "wb").close()
        os.chmod(p, mode)
        return 0

    # symlink support
    def symlink(self, target, source):
        os.symlink(target, self._p(source))

    def readlink(self, path):
        return os.readlink(self._p(path))

def main(mountpoint):
    os.makedirs(ROOT, exist_ok=True)
    os.makedirs(mountpoint, exist_ok=True)
    FUSE(MiniFS(), mountpoint, foreground=True, allow_other=True)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: minisfs.py <mountpoint>")
        raise SystemExit(2)
    main(sys.argv[1])
