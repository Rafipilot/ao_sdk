# Changelog

## 0.1.0-alpha.1 (2025-04-19)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/Rafipilot/ao_sdk/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **client:** allow passing `NotGiven` for body ([#4](https://github.com/Rafipilot/ao_sdk/issues/4)) ([5bac35d](https://github.com/Rafipilot/ao_sdk/commit/5bac35d912ac8589cf00902f90836f3d4ce4ab9c))


### Bug Fixes

* **ci:** ensure pip is always available ([#16](https://github.com/Rafipilot/ao_sdk/issues/16)) ([f01a0a2](https://github.com/Rafipilot/ao_sdk/commit/f01a0a27f1b492e8d641f648e0f03f090b623b1a))
* **ci:** remove publishing patch ([#17](https://github.com/Rafipilot/ao_sdk/issues/17)) ([8edb467](https://github.com/Rafipilot/ao_sdk/commit/8edb4671728e5c6200c57053b7a8549a58d5a481))
* **client:** mark some request bodies as optional ([5bac35d](https://github.com/Rafipilot/ao_sdk/commit/5bac35d912ac8589cf00902f90836f3d4ce4ab9c))
* **perf:** optimize some hot paths ([8343c0e](https://github.com/Rafipilot/ao_sdk/commit/8343c0e1b815a8bef41bacf72cadba3c1901c36f))
* **perf:** skip traversing types for NotGiven values ([49906ff](https://github.com/Rafipilot/ao_sdk/commit/49906ffcb7cddd564360c7bcfa06eed6cc812b16))
* **types:** handle more discriminated union shapes ([#15](https://github.com/Rafipilot/ao_sdk/issues/15)) ([359f043](https://github.com/Rafipilot/ao_sdk/commit/359f0438e8d7a9e05934cb7897d8b6a0c8f6c236))


### Chores

* **client:** minor internal fixes ([2aefaa3](https://github.com/Rafipilot/ao_sdk/commit/2aefaa34359a93c9d591bfe5fa5ccb9470cce37a))
* **docs:** update client docstring ([#8](https://github.com/Rafipilot/ao_sdk/issues/8)) ([57c9b49](https://github.com/Rafipilot/ao_sdk/commit/57c9b491787dab442c16245ffedfb67c03e676f1))
* fix typos ([#18](https://github.com/Rafipilot/ao_sdk/issues/18)) ([7c28706](https://github.com/Rafipilot/ao_sdk/commit/7c28706ffaef4bfc4b80d61ef3db7498e439d54e))
* go live ([#1](https://github.com/Rafipilot/ao_sdk/issues/1)) ([47a3621](https://github.com/Rafipilot/ao_sdk/commit/47a36211655db28749ce79f2773be04b4f5ff699))
* **internal:** base client updates ([8428339](https://github.com/Rafipilot/ao_sdk/commit/842833922ffdffdc7ec5466c65e3346c8bed2fbd))
* **internal:** bump pyright version ([10db997](https://github.com/Rafipilot/ao_sdk/commit/10db997433c12175c5be23b40eba92b20ed3bdbe))
* **internal:** bump rye to 0.44.0 ([#14](https://github.com/Rafipilot/ao_sdk/issues/14)) ([b39fdd1](https://github.com/Rafipilot/ao_sdk/commit/b39fdd1bb32b4b7ef9966ce3cc8a694a2035b923))
* **internal:** codegen related update ([#13](https://github.com/Rafipilot/ao_sdk/issues/13)) ([a977fc1](https://github.com/Rafipilot/ao_sdk/commit/a977fc1cd2598b70ba58f9c7780a6c5533f71f7a))
* **internal:** expand CI branch coverage ([c010869](https://github.com/Rafipilot/ao_sdk/commit/c0108695f38878cfd10a04427a32746490bad918))
* **internal:** fix devcontainers setup ([#5](https://github.com/Rafipilot/ao_sdk/issues/5)) ([b2de6a9](https://github.com/Rafipilot/ao_sdk/commit/b2de6a97c62ef7f5d0eaca746fee05e67895ca2c))
* **internal:** properly set __pydantic_private__ ([#6](https://github.com/Rafipilot/ao_sdk/issues/6)) ([67aacbd](https://github.com/Rafipilot/ao_sdk/commit/67aacbdf6c14cc31e44a1715eadef948fb78e75b))
* **internal:** reduce CI branch coverage ([22bec5b](https://github.com/Rafipilot/ao_sdk/commit/22bec5bf9326a1163aa720df07c9f4f0779c0569))
* **internal:** remove extra empty newlines ([#12](https://github.com/Rafipilot/ao_sdk/issues/12)) ([b58fa2f](https://github.com/Rafipilot/ao_sdk/commit/b58fa2f522b5e545fa78e349929f55db090d81f4))
* **internal:** remove trailing character ([#19](https://github.com/Rafipilot/ao_sdk/issues/19)) ([8157b68](https://github.com/Rafipilot/ao_sdk/commit/8157b68ac7a6d1babd6e39acd38c6bd64837e490))
* **internal:** remove unused http client options forwarding ([#9](https://github.com/Rafipilot/ao_sdk/issues/9)) ([db32a00](https://github.com/Rafipilot/ao_sdk/commit/db32a00c4daa1e580c654ce7f5892f535b2091b9))
* **internal:** slight transform perf improvement ([#20](https://github.com/Rafipilot/ao_sdk/issues/20)) ([1042fb9](https://github.com/Rafipilot/ao_sdk/commit/1042fb9321fc6acdd7c30d2b09f234e7f6c69ae5))
* **internal:** update models test ([e480d64](https://github.com/Rafipilot/ao_sdk/commit/e480d6422c12a65ca72fa9b92b83246ca7461f58))
* **internal:** update pyright settings ([3702201](https://github.com/Rafipilot/ao_sdk/commit/37022016c7509b8254accbaefa4be453755dbb71))
* update SDK settings ([#3](https://github.com/Rafipilot/ao_sdk/issues/3)) ([5598ced](https://github.com/Rafipilot/ao_sdk/commit/5598cede83ed29ae0007e877da146549ad16509b))


### Documentation

* revise readme docs about nested params ([#10](https://github.com/Rafipilot/ao_sdk/issues/10)) ([90d5239](https://github.com/Rafipilot/ao_sdk/commit/90d5239953ea9aaf936549ee770d03f3922a76c9))
* update URLs from stainlessapi.com to stainless.com ([#7](https://github.com/Rafipilot/ao_sdk/issues/7)) ([bc83234](https://github.com/Rafipilot/ao_sdk/commit/bc83234ecb0bb612dbf7d847f435645281d15ba2))
