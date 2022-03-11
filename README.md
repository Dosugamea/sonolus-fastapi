# Sonolus-FastApi
![Python Version](https://img.shields.io/badge/python-v3.8-blue)
![License](https://img.shields.io/badge/license-AGPLv3%2B-green)
[![codecov](https://codecov.io/gh/PurplePalette/sonolus-fastapi/branch/master/graph/badge.svg?token=YGBF0S2VGL)](https://codecov.io/gh/PurplePalette/sonolus-fastapi)

Third public Sonolus api to manage user generated background, effect, engine, level, particle and skin. Sure it accepts user upload and, able to deliver the contents to sonolus client.

## Requirements

* Poetry(>=1.16)
* Python(>=3.8.x)
* Firebase Authorization
* MySQL or MariaDB Server
* [SUS Conversion Server](https://github.com/PurplePalette/sonolus-sus-server)
* Any S3 storage(Recommends [B2 Cloud Storage](https://www.backblaze.com/b2/cloud-storage.html) with [Cloudflare](https://cloudflare.com/))
* Any VPS(Recommends [Oracle Cloud Free Tier](https://www.oracle.com/jp/cloud/free/))

## Production setup
Please refer [wiki article](https://github.com/PurplePalette/sonolus-fastapi/wiki/Production-setup)

## Development setup
Please refer [wiki article](https://github.com/PurplePalette/sonolus-fastapi/wiki/Development-Setup)

## Docs
- [API Spec / Stoplight](https://sonolus-core.stoplight.io/docs/servers/YXBpOjM2MTAxMzcx-sweet-potato-server-3-api)
- [Detailed spec, frontend mock / Whimsical](https://whimsical.com/sweet-potato-next-2EyH4Ts7UBT6t2cpwmKdR4)

## Powered by OpenAPI
This server was generated by the [openapi-generator](https://openapi-generator.tech) project.
By using the [OpenAPI-Spec](https://github.com/OAI/OpenAPI-Specification) from a remote server, you can easily generate a server stub. To see how to make this your own, look these: [README](https://openapi-generator.tech) / [ServerSpec](https://github.com/PurplePalette/sonolus-fastapi/blob/master/openapi.yaml) / [ServerSpec(Stoplight)](https://sonolus-core.stoplight.io/docs/servers/YXBpOjM2MTAxMzcx-sweet-potato-server-3-api)
- API version: 1.0
- Build package: org.openapitools.codegen.languages.PythonFastAPIServerCodegen
- For more information, please visit [https://discord.gg/KEfVkfC6Q9](https://discord.gg/KEfVkfC6Q9)