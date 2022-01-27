# coding: utf-8

"""
    SweetPotato Server 3 API

    Advanced Sonolus API server with adds many features (Python)
    Development repository:
    https://github.com/PurplePalette/sonolus-fastapi

    The version of the OpenAPI document: 0.5.10
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.apis.accounts_backgrounds_api import router as AccountsBackgroundsApiRouter
from src.apis.accounts_effects_api import router as AccountsEffectsApiRouter
from src.apis.accounts_engines_api import router as AccountsEnginesApiRouter
from src.apis.accounts_info_api import router as AccountsInfoApiRouter
from src.apis.accounts_levels_api import router as AccountsLevelsApiRouter
from src.apis.accounts_levels_specials_api import (
    router as AccountsLevelsSpecialsApiRouter,
)
from src.apis.accounts_particles_api import router as AccountsParticlesApiRouter
from src.apis.accounts_skins_api import router as AccountsSkinsApiRouter
from src.apis.announces_api import router as AnnouncesApiRouter
from src.apis.default_backgrounds_api import router as DefaultBackgroundsApiRouter
from src.apis.default_effects_api import router as DefaultEffectsApiRouter
from src.apis.default_engines_api import router as DefaultEnginesApiRouter
from src.apis.default_info_api import router as DefaultInfoApiRouter
from src.apis.default_levels_api import router as DefaultLevelsApiRouter
from src.apis.default_levels_specials_api import (
    router as DefaultLevelsSpecialsApiRouter,
)
from src.apis.default_particles_api import router as DefaultParticlesApiRouter
from src.apis.default_skins_api import router as DefaultSkinsApiRouter
from src.apis.pickups_api import router as PickupsApiRouter
from src.apis.tests_backgrounds_api import router as TestsBackgroundsApiRouter
from src.apis.tests_effects_api import router as TestsEffectsApiRouter
from src.apis.tests_engines_api import router as TestsEnginesApiRouter
from src.apis.tests_info_api import router as TestsInfoApiRouter
from src.apis.tests_levels_api import router as TestsLevelsApiRouter
from src.apis.tests_particles_api import router as TestsParticlesApiRouter
from src.apis.tests_skins_api import router as TestsSkinsApiRouter
from src.apis.uploads_api import router as UploadsApiRouter
from src.apis.users_api import router as UsersApiRouter
from src.apis.users_backgrounds_api import router as UsersBackgroundsApiRouter
from src.apis.users_effects_api import router as UsersEffectsApiRouter
from src.apis.users_engines_api import router as UsersEnginesApiRouter
from src.apis.users_info_api import router as UsersInfoApiRouter
from src.apis.users_levels_api import router as UsersLevelsApiRouter
from src.apis.users_particles_api import router as UsersParticlesApiRouter
from src.apis.users_skins_api import router as UsersSkinsApiRouter
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SweetPotato Server 3 API",
    description="Advanced Sonolus API server with adds many features (Python)",
    version="0.5.10",
)

origins = [
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AccountsBackgroundsApiRouter)
app.include_router(AccountsEffectsApiRouter)
app.include_router(AccountsEnginesApiRouter)
app.include_router(AccountsInfoApiRouter)
app.include_router(AccountsLevelsApiRouter)
app.include_router(AccountsLevelsSpecialsApiRouter)
app.include_router(AccountsParticlesApiRouter)
app.include_router(AccountsSkinsApiRouter)
app.include_router(AnnouncesApiRouter)
app.include_router(DefaultBackgroundsApiRouter)
app.include_router(DefaultEffectsApiRouter)
app.include_router(DefaultEnginesApiRouter)
app.include_router(DefaultInfoApiRouter)
app.include_router(DefaultLevelsApiRouter)
app.include_router(DefaultLevelsSpecialsApiRouter)
app.include_router(DefaultParticlesApiRouter)
app.include_router(DefaultSkinsApiRouter)
app.include_router(PickupsApiRouter)
app.include_router(TestsBackgroundsApiRouter)
app.include_router(TestsEffectsApiRouter)
app.include_router(TestsEnginesApiRouter)
app.include_router(TestsInfoApiRouter)
app.include_router(TestsLevelsApiRouter)
app.include_router(TestsParticlesApiRouter)
app.include_router(TestsSkinsApiRouter)
app.include_router(UploadsApiRouter)
app.include_router(UsersApiRouter)
app.include_router(UsersBackgroundsApiRouter)
app.include_router(UsersEffectsApiRouter)
app.include_router(UsersEnginesApiRouter)
app.include_router(UsersInfoApiRouter)
app.include_router(UsersLevelsApiRouter)
app.include_router(UsersParticlesApiRouter)
app.include_router(UsersSkinsApiRouter)
app.mount("/", StaticFiles(directory="src/static"), name="static")
