from project import project


#user router
from endpoint.coal import router as coal_router
project.include_router(coal_router)
