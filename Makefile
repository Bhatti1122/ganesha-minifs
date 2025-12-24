up:
	cd ganesha && bash setup.sh

run-minifs:
	cd minisfs && sudo -E bash -c "./run.sh"

export:
	sudo systemctl restart nfs-ganesha

mount:
	cd client && bash mount_nfs.sh

test:
	cd client && pytest -q

bench:
	cd bench && bash fio_smoke.sh

clean:
	- sudo umount /mnt/nfsmini || true
