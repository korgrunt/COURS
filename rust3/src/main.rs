use pcap::Capture;
use packet::Packet;
use dns_parser::Packet as PacketDsn;

fn main() {

    let mut pcapFile = Capture::from_file("/home/naouaichia/Workspace/COURS/rust3/dns.cap").expect("can't re");
    
    while let Ok(packet) = pcapFile.next_packet() {
        let eth_packet = packet::ether::Packet::new(packet.data).unwrap();
        let ip_packet = packet::ip::v4::Packet::new(eth_packet.payload()).unwrap();
        let udp_packet = packet::udp::Packet::new(ip_packet.payload()).unwrap();

        
        if let Ok(dns_packet) = dns_parser::Packet::parse(udp_packet.payload()) {
            for question in dns_packet.questions {
                println!("{:?}", question.qname);
            }
        }
    }
}
