build:
	docker build -t property-price-analyzer:latest .

run:
	docker run -it --name property-price-analyzer-scheduler property-price-analyzer:latest

