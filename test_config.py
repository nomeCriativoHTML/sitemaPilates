from app.core.config import settings

print("🔧 TESTANDO CONFIGURAÇÃO:")
print(f"DATABASE_URL carregada: {settings.DATABASE_URL is not None}")
if settings.DATABASE_URL:
    print(f"URL: {settings.DATABASE_URL}")

# Teste de conexão básica
try:
    from sqlalchemy import create_engine, text
    engine = create_engine(settings.DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version()"))
        print(f"✅ PostgreSQL Version: {result.scalar()}")
        print("🎉 Conexão com PostgreSQL bem-sucedida!")
except Exception as e:
    print(f"❌ Erro de conexão: {e}")
    print("\n🔧 Possíveis soluções:")
    print("1. Verifique se o PostgreSQL está rodando")
    print("2. Confirme se o usuário 'root' e senha 'root' estão corretos")
    print("3. Verifique se o database 'pilates_db' existe")