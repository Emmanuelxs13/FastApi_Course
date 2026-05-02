# Modelo base para una película


from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: int
    title: str
    year: int
    category: str

# Modelo para crear una película, con validaciones


class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15)
    year: int = Field(ge=1900, le=2024)
    category: str = Field(min_length=5, max_length=20)

    # Ejemplo de datos para la documentación
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 4,
                "title": "TheMatrix",
                "year": 1999,
                "category": "Sci-Fi"
            }
        }
    }

# Modelo para actualizar una película


class MovieUpdate(BaseModel):
    title: str
    year: int
    category: str