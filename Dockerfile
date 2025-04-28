# ---------- Stage 1: Build environment ----------
    FROM python:3.12-slim AS builder

    WORKDIR /app
    
    # Install build dependencies
    RUN apt-get update && apt-get install -y build-essential libpq-dev
    
    # Install pip packages in isolated layer
    COPY requirements.txt .
    RUN pip install --upgrade pip
    RUN pip install --user -r requirements.txt
    
    # ---------- Stage 2: Runtime image ----------
    FROM python:3.12-slim
    
    WORKDIR /app
    
    # Copy only necessary files
    COPY --from=builder /root/.local /root/.local
    COPY app.py .
    ENV PATH=/root/.local/bin:$PATH
    
    # Expose port
    EXPOSE 3000
    
    # Run FastAPI app with Uvicorn
    CMD ["python3", "app.py"]
    