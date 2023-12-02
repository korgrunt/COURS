use url::{Url};

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let val1: String = args[1].parse().expect("Bad parsing for u32");
    let issue_list_url = Url::parse(&val1);
    let binding = issue_list_url.expect("Can't retrieve url");
    let parsed_http_query= binding.query_pairs();

    for elm in parsed_http_query {
        println!("query param {:?} => : value : =>{:?}", elm.0, elm.1);
    }

}
