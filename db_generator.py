import random
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


# Définir la configuration de la base de données
database_uri = "mysql://root@127.0.0.1:3306/bigdata"
engine = create_engine(database_uri)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Définir les modèles de tables
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100))

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)

# Générer un grand nombre d'utilisateurs et de produits
def generate_data():
    session = Session()

    for _ in range(1000000):  # Changer ce nombre pour générer plus ou moins de données
        user = User(
            name=f"Utilisateur {random.randint(1, 1000000)}",
            age=random.randint(18, 99),
            email=f"user{random.randint(1, 1000000)}@example.com"
        )
        session.add(user)

        product = Product(
            name=f"Produit {random.randint(1, 1000000)}",
            price=random.randint(1, 1000)
        )
        session.add(product)

    session.commit()
    session.close()

# Créer les tables dans la base de données
Base.metadata.create_all(engine)

# Générer les données
generate_data()
