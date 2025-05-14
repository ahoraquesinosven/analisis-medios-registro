import tldextract
from urllib.parse import urlparse, urlunparse, quote, unquote, parse_qs

# TESTING Parse a URL
url = "https://otrasvocesmdz.com.ar/brutal-intento-de-femicidio-en-el-palomar-apunalo-a-su-ex-pareja-y-huyo/"
parsed_url = urlparse(url)
print("Netloc:", parsed_url.netloc)

extracted_info = tldextract.extract(parsed_url.netloc)
print("Extracted info: ",extracted_info)

#Obtener domain
def get_url_domain(url):
    parsed_url = urlparse(url)
    extracted_info = tldextract.extract(parsed_url.netloc)
    return extracted_info.domain

# TODO abrir CSV y por cada row, obtener mes y año,  provincia, category y domain
# TODO group by domain





# # Encode a query string
# query_string = "data with spaces and & characters"
# encoded_query = quote(query_string)
# print("Encoded query:", encoded_query)

# # Decode a query string
# decoded_query = unquote(encoded_query)
# print("Decoded query:", decoded_query)

# # Parse query parameters
# query_params = parse_qs(parsed_url.query)
# print("Query parameters:", query_params)
