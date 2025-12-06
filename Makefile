build-HelloWorldFunction:
	mkdir -p $(ARTIFACTS_DIR)
	uv pip install -r requirements.txt --target $(ARTIFACTS_DIR)
	cp -R hello_world $(ARTIFACTS_DIR)
