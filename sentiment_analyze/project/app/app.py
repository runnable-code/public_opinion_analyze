from fastapi import FastAPI

from project.app.exceptions.exception_handlers import register_exception_handlers
from project.app.routers.hello import router
from project.app.routers import system, event_router, report, research
from project.app.services.lifecycle import lifecycle_manager

async def lifespan(app: FastAPI):
    """应用启停时注册与关闭生命周期管理器"""
    try:
        lifecycle_manager.register()
        yield
    finally:
        await lifecycle_manager.shutdown()


app = FastAPI(description="FASTAPI实例", lifespan=lifespan)
app.include_router(router)
app.include_router(system.router)

app.include_router(report.router)
app.include_router(research.router)
app.include_router(event_router.router)

register_exception_handlers(app)
