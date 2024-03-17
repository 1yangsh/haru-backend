export PYTHONPATH=.
.DEFAULT_GOAL:=help

.PHONY: format
format:  ## 🔧 코드를 포매팅합니다.
	pycln . --all
	black .
	isort .

.PHONY: run-server
run-server:  ## 🚀 REST 서버를 실행합니다.
	python src/main.py

.PHONY: test
test:  ## 🧪 테스트를 진행합니다.
	pytest tests


.PHONY: help
help:  ## ❓  사용 가능한 커멘드를 확인합니다
	@echo 'usage: make [command]'
	@echo
	@echo 'command:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'