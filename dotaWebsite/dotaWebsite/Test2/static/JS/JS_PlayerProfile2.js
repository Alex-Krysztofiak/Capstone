class MyProfileDisplay extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            matches: [],
            matchIndex: 0,
            heroes: [],
            heroesIndex: 0,
            profile: [],
            peerIndex: 0,
            peers: [],
            mostplayedIndex: 0,
            mostplayed: [],
        }
    }




    componentDidMount() {
        fetch('static\\JSON\\heroList.json')
            .then(response => response.json())
            .then(data2 => this.setState({ heroes: data2, isLoading: false }));
        fetch('static\\JSON\\matches_recent.json')
            .then(response => response.json())
            .then(data => this.setState({ matches: data, isLoading: false }));
        fetch('static\\JSON\\PlayerProfile.json')
            .then(response => response.json())
            .then(data => this.setState({ profile: data, isLoading: false }));
        fetch('static\\JSON\\peer_info.json')
            .then(response => response.json())
            .then(data => this.setState({ peers: data, isLoading: false }));
        fetch('static\\JSON\\mostplayed_info.json')
            .then(response => response.json())
            .then(data => this.setState({ mostplayed: data, isLoading: false }));
    }

    render() {
        if (this.state.isLoading) {
            return (<p>Loading ....</p>)
        } else {
            return (
                
                <>
                     <table key="profile" className="playerProfile">
                        <tbody>
                        {
                            this.state.profile.map(profile => {
                                return (
                                    <>
                                    <tr>
                                        <td key={"key_" + profile.id} className="playerProfileInfo">
                                            <img key={"imgkey_" + profile.id} src={profile.avatar}></img>
                                        </td>
                                        <td key={"key_" + profile.id} className="playerProfileInfo">
                                            <h1>{profile.name}</h1>
                                            <h3>{profile.id}</h3>
                                        </td>
                                        <td key={"key_" + profile.id} className="playerProfileInfo">
                                            <h2>Wins: {profile.wins}</h2>
                                            <h2>Losses: {profile.losses}</h2>
                                            <h2>Winrate: {profile.wr}</h2>
                                        </td>
                                        <td key={"key_" + profile.id} className="playerProfileInfo">
                                            {(() => {
                                                switch (profile.rank_name) {
                                                    case 1:
                                                        return "Herald: ";
                                                    case 2:
                                                        return "Guardian: ";
                                                    case 3:
                                                        return "Crusader: ";
                                                    case 4:
                                                        return "Archon: ";
                                                    case 5:
                                                        return "Legend: ";
                                                    case 6:
                                                        return "Ancient: ";
                                                    case 7:
                                                        return "Divine: ";
                                                    case 8:
                                                        return "Immortal: ";
                                                    default:
                                                        return "unranked";
                                                }
                                            })()}
                                            {profile.rank_number}
                                            
                                            <h2>MMR: {profile.rank_estimate}</h2>
                                        </td>
                                        <td key={"key_" + profile.id} className="playerProfileInfo">
                                            {(() => {
                                                switch (profile.rank_name) {
                                                    case 1:
                                                        return <img src="https://dota2freaks.com/wp-content/uploads/sites/10/2020/02/dota-2-rank-herald1.png"></img>
                                                    case 2:
                                                        return <img src="https://dota2freaks.com/wp-content/uploads/sites/10/2020/02/dota-2-rank-guardian-1.png"></img>
                                                    case 3:
                                                        return <img src="https://dota2freaks.com/wp-content/uploads/sites/10/2020/02/dota-2-rank-crusader-1.png"></img>;
                                                    case 4:
                                                        return <img src="https://static.wikia.nocookie.net/dota2_gamepedia/images/a/a3/SeasonalRank4-5.png"></img>;
                                                    case 5:
                                                        return <img src="https://static.wikia.nocookie.net/dota2_gamepedia/images/2/25/SeasonalRank5-4.png"></img>;
                                                    case 6:
                                                        return <img src="https://cdn-0.dota2freaks.com/wp-content/uploads/sites/10/2020/02/dota-2-rank-ancient-3.png"></img>;
                                                    case 7:
                                                        return <img src="https://static.wikia.nocookie.net/dota2_gamepedia/images/b/b7/SeasonalRank7-1.png"></img>
                                                    case 8:
                                                        return <img src="https://static.wikia.nocookie.net/dota2_gamepedia/images/a/ad/SeasonalRankTop2.png"></img>
                                                    default:
                                                        return <img src="https://cdn.shopify.com/s/files/1/2312/2697/products/cali_3.png?v=1576660156"></img>
                                                }
                                            })()}
                                            </td>
                                        </tr>

                                    </>
                                )
                            })}
                    </tbody>
                    </table> 
                    <>
                    <table className="MatchesTable">
                            <caption>Recent Matches</caption>
                                    <thead>
                                        <tr>
                                        <th>Hero</th>
                                        <th>{/* Blank */}</th>
                                        <th>Duration</th>
                                        <th>K / D / A</th>
                                        {/* <th>D</th>
                                        <th>A</th> */}
                                        <th>Result</th>
                                        <th>Party Size</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                    {
                        this.state.matches.map(match => {
                            return (
                                <>
                                <tr key={match.match_id} className="gameInfoBox">
                                    <td key={"key_" + match.match_id + match.hero_name} className="matchInfo">
                                          
                                        {this.state.heroes.map(hero => {
                                            if (match.hero_name == hero.name) {
                                                return (
                                                    <>
                                                        <img key={"key_" + hero.id} src={hero.img}></img>
                                                    </>
                                                )
                                            }
                                        })}
                                          
                                        </td>
                                        <td key={"key_" + match.match_id + match.hero_name} className="matchInfo">
                                            {match.hero_name}
                                        </td>
                                        <td key={"key_" + match.match_id + match.duration} className="matchInfo">
                                            {match.duration}
                                        </td>
                                        <td key={"key_" + match.match_id + match.kills} className="matchInfo">
                                            {match.kills}{" / "}{match.deaths}{" / "}{match.assists}
                                        </td>
                                        {/* <td key={"key_" + match.match_id + match.deaths} className="matchInfo">
                                            {match.deaths}
                                        </td>
                                        <td key={"key_" + match.match_id+ match.assists} className="matchInfo">
                                            {match.assists}
                                        </td> */}
                                        <td key={"key_" + match.match_id} className="matchInfo">
                                            {match.team} <br></br>
                                            {match.result}
                                        </td>
                                        <td key={"key_" + match.match_id + match.party_size} className="matchInfo">
                                            {match.party_size}
                                        </td>
                                    </tr>
                                </>
                            )//match return of the if inside map 
                        })}
                        </tbody>
                        </table>
                        </>


                     <table className="PeerTable">
                        <caption>Peers</caption>

                                <thead>
                                    <tr>
                                    <th>Player</th>
                                    <th></th>
                                    <th>Matches Played</th>
                                    <th>Win Rate %</th>
                                    </tr>
                                </thead>
                                <tbody>
                        {
                        this.state.peers.map(peer => {
                            return (
                                <>   
                                    <tr key={peer.account_id} className="peerInfoBox" id={peer.account_id}>

                                        <td key={"key_" + peer.account_id} className="peerInfo">
                                            <img key={"imgkey_" + peer.avatarfull} src={peer.avatarfull}></img>
                                            
                                        </td>   
                                        <td key={"key_" + peer.account_id + peer.with_games} className="peerInfo">
                                            {peer.personaname}
                                        </td>                               
                                        <td key={"key_" + peer.account_id + peer.with_games} className="peerInfo">
                                            {peer.with_games}
                                        </td>
                                        <td key={"key_" + peer.account_id + peer.with_wr} className="peerInfo">
                                            {peer.with_wr}
                                        </td>
                                       
                                    </tr>
                                    
                                </>
                            )//match return of the if inside map 
                        })}
                        </tbody>
                        </table>

                        <table className="MPTable">
                            <caption>Matches Played</caption>
                                    <thead>
                                        <tr>
                                        <th>HERO</th>
                                        <th></th>
                                        <th>MATCHES</th>
                                        <th>WIN RATE %</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                        {
                        this.state.mostplayed.map(mp => {
                            return (
                                <>
                                    
                                    
                                    
                                    <tr key={mp.hero_id} className="mpInfoBox" id={mp.hero_id}>

                                        <td key={"key_" + mp.hero_id} className="mpInfo">
                                            {this.state.heroes.map(hero => {
                                                if (mp.hero_name == hero.name) {
                                                    return (
                                                        <>
                                                            <img key={"key_" + hero.id} src={hero.img}></img>
                                                            
                                                        </>
                                                    )
                                                }
                                            })}
                                        </td>
                                        <td key={"key_" + mp.games} className="mpInfo">
                                            {mp.hero_name}
                                        </td>
                                        <td key={"key_" + mp.games} className="mpInfo">
                                            {mp.games}
                                        </td>
                                        <td key={"key_" + mp.wr} className="mpInfo">
                                            {mp.wr}
                                        </td>
                                       
                                    </tr>
                                    
                                    
                                </>
                            )//match return of the if inside map 
                        })}
                        </tbody>
                        </table>


                </>

            ) //match return in else of isLoading 

        } //match else of isLoading
    }


}
ReactDOM.render(<MyProfileDisplay />, document.querySelector('#divRecentMatchDisplay'))

