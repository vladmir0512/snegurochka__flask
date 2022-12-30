def FileSizeLimit(max_size_in_mb):
    max_bytes = max_size_in_mb*1024*1024
    def file_length_check(form, field):
        if field.data:
            
            if len(field.data.read()) > max_bytes:
                raise ValidationError(f"File size must be less than {max_size_in_mb}MB")
            field.data.seek(0)
            
        
    return file_length_check    

