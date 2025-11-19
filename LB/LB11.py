from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Median Calculator API")

class NumbersRequest(BaseModel):
    values: List[float]

class MedianResponse(BaseModel):
    median: Optional[float]

def calculate_median(numbers: List[float]) -> Optional[float]:
    """Вычисляет медиану списка чисел"""
    if not numbers:
        return None
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

@app.post(
    "/median",
    response_model=MedianResponse,
    description="Вычисляет медиану переданного списка чисел. Медиана - это среднее значение в отсортированном списке. Для списка с четным количеством элементов берется среднее арифметическое двух центральных элементов."
)
async def calculate_median_endpoint(request: NumbersRequest):
    median_value = calculate_median(request.values)
    return MedianResponse(median=median_value)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)