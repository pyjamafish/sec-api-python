from sec_api.index import RenderApi, XbrlApi, ExtractorApi

#
# Render API
#
"""
renderApi = RenderApi("YOUR_API_KEY")

# 10-K HTM File URL example
filing_data = renderApi.get_filing(
    url="https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm"
)

print(filing_data)
"""

#
# XBRL-to-JSON API example
#
"""
xbrlApi = XbrlApi("YOUR_API_KEY")


# 10-K HTM File URL example
xbrl_json_1 = xbrlApi.xbrl_to_json(
    htm_url="https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm"
)

print(xbrl_json_1["StatementsOfIncome"])
print(xbrl_json_1["BalanceSheets"])
print(xbrl_json_1["StatementsOfCashFlows"])

# 10-K XBRL File URL example
xbrl_json_2 = xbrlApi.xbrl_to_json(
    xbrl_url="https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231_htm.xml"
)

# 10-K XBRL File URL example
xbrl_json_3 = xbrlApi.xbrl_to_json(accession_no="0001564590-21-004599")

"""

#
# Extractor API Example
#
"""
extractorApi = ExtractorApi("YOUR_API_KEY")

# Tesla 10-K filing
filing_url = "https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm"

section_text = extractorApi.get_section(filing_url, "1A", "text")
section_html = extractorApi.get_section(filing_url, "1A", "html")

print(section_text)
print(section_html)
"""
