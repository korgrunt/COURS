use std::collections::HashMap;
use reqwest::header::USER_AGENT;
use scraper::{Selector, Html};
fn main() {
    let url = "http://httpforever.com/";


    //headers.insert("Connection".to_string(), "close".to_string());
    println!("{}", "Start program");

    let body = reqwest::blocking::get(url).unwrap()
        .text()
        .unwrap();

    let fragment = Html::parse_fragment(&body);
    let selector_linkedin = Selector::parse("h3").unwrap();
    for element in fragment.select(&selector_linkedin) {
        println!("{:?}", element.first_child().unwrap().html().as_str());
    }
    //let selector_facebook = Selector::parse("/html/body/div[4]/section/div/div/div[1]/ul/li[2]/a").unwrap();
    //let selector_twitter = Selector::parse("/html/body/div[4]/section/div/div/div[1]/ul/li[3]/a").unwrap();
    let input = fragment.select(&selector_linkedin).next().unwrap();
    println!("bar {:?}", input.value().attr("value"));
    //let ul1 = fragment.select(&selector_twitter).next().unwrap();
//    let ul2 = fragment.select(&selector_facebook).next().unwrap();
  //  let ul3= fragment.select(&selector_linkedin).next().unwrap();
    //println!("{:?}", body);
    /*
    let res = match request::get(&url, &mut headers) {
        Ok(res) => res,
        Err(e) => { println!("{}", e); return; }
    };

    println!("{}", res.http_version);
    println!("{}", res.status_code);
    */
}

