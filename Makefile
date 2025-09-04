play:
	npm i
	npm run build
	node dist/index.js --no-enums play.ts -o play-gen.ts
	npx ts-node --logError play-test.ts
	node dist/index.js --no-enums play.ts -o play_gen.py --python-version 3.7
	python3 play-test.py
