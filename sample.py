import requests
import os

uri = "https://ai.kagermanov.com/classify"

openai_key = os.getenv("OPENAI_API_KEY")

headers = {"Content-Type": "application/json"}

data = {
  "path":
  "google.google_local_results",
  "targets": [
    "<div class=\"boho-chic-parent\">        <b class=\"sing-up-for\">BOHO CHIC</b>        <b class=\"lorem-ipsum-dolor\"          >Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do          eiusmod tempor incididunt ut labore et dolore magna aliqua.</b        >        <div class=\"group-container\">          <div class=\"rectangle-container\">            <div class=\"group-child4\"></div>            <b class=\"view-now\">VIEW ALL</b>          </div>        </div>      </div>"
    #"<div jscontroller=\"AtSb\" class=\"w7Dbne\" data-record-click-time=\"false\" id=\"tsuid_25\" jsdata=\"zt2wNd;_;BvbRxs V6f1Id;_;BvbRxw\" jsaction=\"rcuQ6b:npT2md;e3EWke:kN9HDb\" data-hveid=\"CBUQAA\"><div jsname=\"jXK9ad\" class=\"uMdZh tIxNaf\" jsaction=\"mouseover:UI3Kjd\"><div class=\"VkpGBb\"><div class=\"cXedhc\"><a class=\"vwVdIc wzN8Ac rllt__link a-no-hover-decoration\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" tabindex=\"0\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEAE\"><div><div class=\"rllt__details\"><div class=\"dbg0pd\" aria-level=\"3\" role=\"heading\"><span class=\"OSrXXb\">Y Coffee</span></div><div><span class=\"Y0A0hc\"><span class=\"yi40Hd YrbPuc\" aria-hidden=\"true\">4.0</span><span class=\"z3HNkc\" aria-label=\"Rated 4.0 out of 5,\" role=\"img\"><span style=\"width:56px\"></span></span><span class=\"RDApEe YrbPuc\">(418)</span></span> · <span aria-label=\"Moderately expensive\" role=\"img\">€€</span> · Coffee shop</div><div>Nicosia</div><div class=\"pJ3Ci\"><span>Iconic Seattle-based coffeehouse chain</span></div></div></div></a><a class=\"uQ4NLd b9tNq wzN8Ac rllt__link a-no-hover-decoration\" aria-hidden=\"true\" tabindex=\"-1\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEA4\"><g-img class=\"gTrj3e\"><img id=\"pimg_3\" src=\"https://lh5.googleusercontent.com/p/AF1QipPaihclGQYWEJpMpBnBY8Nl8QWQVqZ6tF--MlwD=w184-h184-n-k-no\" class=\"YQ4gaf zr758c wA1Bge\" alt=\"\" data-atf=\"4\" data-frt=\"0\" width=\"92\" height=\"92\"></g-img></a></div></div></div></div>"
  ],
  "openai_key":
  openai_key
}

r = requests.post(url=uri, headers=headers, json=data)

print(r.json()["results"])