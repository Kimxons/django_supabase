from typing import Dict, Any, Optional
from supabase import Client, create_client
from django.conf import settings
from django.core.exceptions import ValidationError
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class SupabaseService:    
    def __init__(self):
        self.client: Optional[Client] = None
        self.table_name = 'myapp_todo'
        
    def get_client(self) -> Client:
        if not self.client:
            try:
                self.client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
            except Exception as e:
                logger.error(f"Failed to initialize Supabase client: {str(e)}")
                raise ConnectionError("Could not connect to Supabase")
        return self.client

    def fetch_todos(self):
        try:
            response = self.get_client().table(self.table_name).select("*").execute()
            return response.data
        except Exception as e:
            logger.error(f"Error fetching todos: {str(e)}")
            raise ConnectionError("Failed to fetch todos from Supabase")

    def create_todo(self, task: str, completed: bool = False):
        if not task or len(task.strip()) == 0:
            raise ValidationError("Task cannot be empty")
            
        try:
            data = {
                "task": task.strip(), 
                "completed": completed,
                "created_at": datetime.utcnow().isoformat() + "Z",
                "updated_at": datetime.utcnow().isoformat() + "Z"
            }
            response = self.get_client().table(self.table_name).insert(data).execute()
            return response.data[0]
        except Exception as e:
            logger.error(f"Error creating todo: {str(e)}")
            raise ConnectionError("Failed to create todo in Supabase")

    def update_todo(self, todo_id: str, data: Dict[str, Any]):
        try:
            if 'id' in data:
                del data['id']
            
            response = self.get_client().table(self.table_name)\
                .update(data)\
                .eq('id', todo_id)\
                .execute()
            
            if response.data:
                return response.data[0]
            else:
                logger.warning(f"No todo found with id {todo_id}")
                raise ValueError(f"No todo found with id {todo_id}")
        except Exception as e:
            logger.error(f"Error updating todo {todo_id}: {str(e)}")
            raise

    def delete_todo(self, todo_id: str):
        try:
            self.get_client().table(self.table_name)\
                .delete()\
                .eq('id', todo_id)\
                .execute()
        except Exception as e:
            logger.error(f"Error deleting todo {todo_id}: {str(e)}")
            raise ConnectionError(f"Failed to delete todo {todo_id}")