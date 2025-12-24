# Ganesha-mini-fs

NFS-Ganesha harness for testing distributed filesystem semantics using a minimal FUSE implementation.

## What It Does

- Implements a minimal FUSE-based filesystem (MiniFS) in Python
- Exports the FUSE filesystem via NFS-Ganesha using the VFS FSAL
- Validates NFSv4 semantics (symlinks, readdir, concurrent operations) over network mount
- Provides automated testing with pytest and performance benchmarking with fio

## Architecture / Key Components

```
┌─────────────┐     NFSv4      ┌──────────────┐     FSAL/VFS    ┌──────────┐
│ NFS Client  │ ────────────> │ NFS-Ganesha  │ ─────────────> │  MiniFS  │
│ /mnt/nfsmini│     (TCP)      │  (userspace) │                 │  (FUSE)  │
└─────────────┘                └──────────────┘                 └──────────┘
                                                                      │
                                                                      v
                                                          /var/tmp/minifs_store
```

**Components:**
- **MiniFS**: Python FUSE filesystem with basic operations (read, write, symlink, readdir)
- **NFS-Ganesha**: Userspace NFS server exporting the FUSE mount via NFSv4
- **Test Suite**: Pytest-based validation of filesystem semantics and concurrency
- **Benchmark**: fio-based I/O performance smoke test (30s, 4K random read/write)

## Tech Stack

- **Language**: Python 3
- **Filesystem**: FUSE (via fusepy)
- **NFS Server**: NFS-Ganesha (VFS FSAL)
- **Testing**: pytest
- **Benchmarking**: fio
- **Platform**: Linux (Ubuntu 22.04+ recommended)

## Prerequisites

Ubuntu 22.04 or later (required for NFS-Ganesha and FUSE kernel support):

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip fuse nfs-ganesha nfs-ganesha-vfs nfs-common python3-pytest fio
pip3 install fusepy
```

**Permissions**: User must have sudo access for mounting filesystems and managing systemd services.

## Quickstart

This setup requires two terminals running concurrently.

**Terminal 1 - Start MiniFS and NFS-Ganesha:**

```bash
# Install and configure NFS-Ganesha
make up

# Start MiniFS (runs in foreground)
make run-minifs
```

**Terminal 2 - Mount and Test:**

```bash
# Restart NFS-Ganesha to apply export
make export

# Mount NFS export locally
make mount

# Run functional tests
make test

# Run I/O benchmark
make bench
```

## Configuration

### Environment Variables

No environment variables required. All paths are hardcoded for single-machine testing.

### Key Paths

| Path | Purpose |
|------|---------|
| `/var/tmp/minifs_store` | MiniFS backing storage |
| `/mnt/minifs` | FUSE mount point |
| `/mnt/nfsmini` | NFS client mount point |
| `/etc/ganesha/ganesha.conf` | NFS-Ganesha main config |
| `/etc/ganesha/exports.conf` | NFS export definition |

### NFS Export Configuration

The NFS export is configured in `ganesha/exports.conf`:
- Export ID: 1
- Path: `/mnt/minifs`
- Pseudo: `/export`
- Access: Read-Write
- Protocol: NFSv4 over TCP
- Clients: 127.0.0.1 only

## How to Run Tests

### Functional Tests

```bash
cd client
pytest -v
```

**Tests validate:**
- Symlink creation and readlink semantics
- Directory listing (readdir) correctness
- File read/write operations
- Concurrent file creation (50 parallel creates)

### Performance Benchmark

```bash
cd bench
bash fio_smoke.sh
```

Runs 30-second fio test with:
- Block size: 4K
- I/O pattern: 70% read, 30% write (random)
- I/O depth: 8
- Engine: psync

## Project Structure

```
ganesha-minifs/
├── Makefile              # Build and test orchestration
├── minisfs/
│   ├── minisfs.py        # FUSE filesystem implementation
│   └── run.sh            # MiniFS startup script
├── ganesha/
│   ├── ganesha.conf      # NFS-Ganesha main configuration
│   ├── exports.conf      # NFS export definition
│   └── setup.sh          # Install and configure Ganesha
├── client/
│   ├── mount_nfs.sh      # NFS mount script
│   └── tests_fs.py       # pytest test suite
└── bench/
    └── fio_smoke.sh      # I/O performance benchmark
```

## Troubleshooting

### MiniFS fails to start
- **Error**: `fusermount: failed to open /dev/fuse: Permission denied`
- **Fix**: Add user to `fuse` group or run with sudo: `sudo usermod -a -G fuse $USER` (requires logout/login)

### NFS mount fails
- **Error**: `mount.nfs4: Connection refused`
- **Fix**: Ensure NFS-Ganesha is running: `sudo systemctl status nfs-ganesha`
- **Fix**: Check firewall allows localhost: `sudo ufw allow from 127.0.0.1`

### Tests fail with "No such file or directory"
- **Error**: Test fails accessing `/mnt/nfsmini`
- **Fix**: Verify NFS is mounted: `mount | grep nfsmini`
- **Fix**: Re-run `make mount`

### Port already in use
- **Error**: `NFS-Ganesha failed to bind port 2049`
- **Fix**: Kill existing NFS processes: `sudo systemctl stop nfs-kernel-server nfs-ganesha`

## Roadmap / Future Improvements

- Add support for file deletion and rename operations
- Implement extended attributes (xattr) support
- Add multi-client testing from separate machines
- Implement NFSv4 ACLs and security flavors (Kerberos)
- Add performance comparison vs kernel NFS server
- Create Docker container for isolated testing
- Add CI/CD pipeline with GitHub Actions

## License

TBD
