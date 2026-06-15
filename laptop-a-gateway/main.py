def minio_webhook(request):
    """Dipanggil waktu ada event dari MinIO"""
    data = request.get_json(silent=True) or {}
    bucket = data.get('bucket', 'unknown')
    file = data.get('file', 'unknown')
    print(f"[GCP Function] File {file} uploaded to {bucket}")
    return f"OK: processed {file} in {bucket}", 200
