from urllib.parse import urlparse, urlunparse, quote, unquote, parse_qs
import tldextract

# Parse a URL
url = "https://otrasvocesmdz.com.ar/brutal-intento-de-femicidio-en-el-palomar-apunalo-a-su-ex-pareja-y-huyo/"
parsed_url = urlparse(url)
print("Netloc:", parsed_url.netloc)

extracted_info = tldextract.extract(parsed_url.netloc)
print("Extracted info: ",extracted_info)


print("Scheme:", parsed_url.scheme)
print("Netloc:", parsed_url.netloc) # lo que necesito
print("Path:", parsed_url.path)
# print("Params:", parsed_url.params)
# print("Query:", parsed_url.query)
# print("Fragment:", parsed_url.fragment)

def get_url_netloc(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc






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
