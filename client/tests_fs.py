import os, subprocess

NFS = "/mnt/nfsmini"

def test_symlink_readlink_readdir():
    os.makedirs(f"{NFS}/fsops", exist_ok=True)
    tgt = f"{NFS}/fsops/target.txt"
    with open(tgt, "w") as f:
        f.write("hello\n")
    lnk = f"{NFS}/fsops/ln_target"
    if os.path.lexists(lnk):
        os.remove(lnk)
    os.symlink(tgt, lnk)
    assert os.readlink(lnk) == tgt
    assert {"target.txt","ln_target"}.issubset(set(os.listdir(f"{NFS}/fsops")))
    with open(lnk) as f:
        assert f.readline().strip() == "hello"

def test_crud_and_concurrency():
    os.makedirs(f"{NFS}/conc", exist_ok=True)
    subprocess.check_call("bash -lc 'for i in {1..50}; do echo $i > /mnt/nfsmini/conc/f$i & done; wait'", shell=True)
    assert len(os.listdir(f"{NFS}/conc")) == 50
