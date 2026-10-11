up:
	docker build -t my_fastapy_app .
	docker run -d --name my_fastapi_container -p 8000:8000 my_fastapy_app

down:
	docker stop my_fastapi_container || true
	docker rm my_fastapi_container || true
	docker rmi my_fastapy_app || true

clean:
	sudo fuser -k 8000/tcp