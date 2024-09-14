from fastapi import Request
from fastapi.responses import JSONResponse
from keycloak import KeycloakOpenID
import os

# 환경 변수 사용
KEYCLOAK_URL = os.getenv("KEYCLOAK_URL")
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM")
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")

print(f"===================> KEYCLOAK_URL: {KEYCLOAK_URL}")
print(f"===================> KEYCLOAK_REALM: {KEYCLOAK_REALM}")
print(f"===================> KEYCLOAK_CLIENT_ID: {KEYCLOAK_CLIENT_ID}")
print(f"===================> KEYCLOAK_CLIENT_SECRET: {KEYCLOAK_CLIENT_SECRET}")

# Keycloak 클라이언트 인스턴스 생성
keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_URL,
    client_id=KEYCLOAK_CLIENT_ID,
    realm_name=KEYCLOAK_REALM,
    client_secret_key=KEYCLOAK_CLIENT_SECRET
)

# 인티로스펙션 함수
##def introspect_token(token: str):
##    return keycloak_openid.introspect(token, token_type_hint='access_token')

def verify_token(token):
    try:
        # Decode token with signature verification
        decoded_token = keycloak_openid.decode_token(token)
        print(decoded_token)
        return decoded_token
    except Exception as e:
        return None

async def jwt_middleware(request: Request, call_next):
    try:
        # Extract the Authorization header
        authorization: str = request.headers.get("Authorization")
        if not authorization:
            return JSONResponse(status_code=401, content={"detail": "Authorization header is missing"})

        # Extract the token, assuming it's a Bearer token
        try:
            token = authorization.split(" ")[1]
        except IndexError:
            return JSONResponse(status_code=401, content={"detail": "Bearer token malformed"})

        # Verify the token
        introspection_result = verify_token(token)
        if introspection_result is None:
            return JSONResponse(status_code=401, content={"detail": "Token is invalid or expired"})

        # If token is valid, proceed with the request
        response = await call_next(request)
        return response
    except Exception as e:
        # Catch any unexpected exceptions and convert to server error response
        return JSONResponse(status_code=500, content={"detail": str(e)})
