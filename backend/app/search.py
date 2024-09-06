from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models import Contact

class ContactSearch:
    def __init__(self, db: Session):
        self.db = db
    
    def full_text_search(self, query: str, user_id: int, limit: int = 50):
        # Using PostgreSQL full text search
        search_vector = func.to_tsvector('english', Contact.name) |                        func.to_tsvector('english', Contact.email)
        
        query_vec = func.plainto_tsquery('english', query)
        
        results = self.db.query(Contact).filter(
            Contact.user_id == user_id,
            search_vector.match(query_vec)
        ).limit(limit).all()
        
        return results
    
    def faceted_search(self, user_id: int, filters: dict):
        query = self.db.query(Contact).filter(Contact.user_id == user_id)
        
        if "name" in filters:
            query = query.filter(Contact.name.ilike(f"%{filters['name']}%"))
        
        if "email" in filters:
            query = query.filter(Contact.email.ilike(f"%{filters['email']}%"))
        
        if "phone" in filters:
            query = query.filter(Contact.phone == filters['phone'])
        
        return query.all()
    
    def autocomplete(self, query: str, user_id: int, field: str = "name"):
        results = self.db.query(getattr(Contact, field)).filter(
            Contact.user_id == user_id,
            getattr(Contact, field).ilike(f"{query}%")
        ).distinct().limit(10).all()
        
        return [r[0] for r in results]
