class MyMatchDisplay extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            matchinfo: [],
            players: [],
            items: [],
            chats: [],
            heroes: [],
            heroesIndex: 0,
        }
    }



    componentDidMount() {
        fetch('..\\static\\JSON\\match_info.json')
            .then(response => response.json())
            .then(data => this.setState({ matchinfo: data, isLoading: false }));
        fetch('..\\static\\JSON\\player_info.json')
            .then(response => response.json())
            .then(data => this.setState({ players: data, isLoading: false }));
        fetch('..\\static\\JSON\\chat_info.json')
            .then(response => response.json())
            .then(data => this.setState({ chats: data, isLoading: false }));
        
        fetch('..\\static\\JSON\\item_ids.json')
            .then(response => response.json())
            .then(data => this.setState({ items: data["items"], isLoading: false }));
        fetch('..\\static\\JSON\\heroList.json')
            .then(response => response.json())
            .then(data2 => this.setState({ heroes: data2, isLoading: false }));
    }

    render() {
        if (this.state.isLoading) {
            return (<p>Loading ....</p>)
        } else {
            return (
                <>
                    <div key="match" className="playerContainer">
                        {this.state.matchinfo.map(info => {
                            return(
                                <>
                                <div className="something">
                                    <p>{info.match_id}</p>
                                    <p>{info.lobby_type}</p>
                                    <p>{info.duration}</p>
                                    <p>{info.winner}</p>
                                    <p>{info.start_time}</p>
                                    <p>{info.replay_url}</p>
                                </div>
                                </>
                            )
                        })}
                    </div>

                    <div className="RecentMatches" id="2">
                    <table className="MatchesTable">
                            <caption>Radiant</caption>
                                    <thead>
                                        <tr>
                                        <th>Hero</th>
                                        <th>{/* Blank */}</th>
                                        <th>LVL</th>
                                        <th>K / D / A</th>
                                        <th>GPM / XPM</th>
                                        <th>Items</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                        {this.state.players.map(player => {
                            
                                    return (
                                        
                                        <>
                                        {(() => { if (player.player_slot < 120) {
                                            return (
                                        
                                            <tr key={player.id} className="gameInfoBox">
                                                <td key={"key_" + player.account_id} className="matchInfo">
                                                        
                                                    {this.state.heroes.map(hero => {
                                                        if (player.hero_id == hero.id) {
                                                            return (
                                                                <>
                                                                    <img key={"key_" + hero.id} src={hero.img}></img>
                                                                </>
                                                        )}
                                                    })}
                                                </td>
                                                <td key={"key_" + player.account_id} id={player.account_id} className="matchInfo">

                                                {(() => {
                                                    switch (player.account_id) {
                                                        case "private":
                                                            return <a id={player.account_id}>{player.personaname}</a>
                                                        default:
                                                            return <a href={"/player_" + player.account_id} id={player.account_id}>{player.personaname}</a>
                                                    }
                                                })()}
                                                    
                                                    
                                                </td>
                                                <td key={"key_" + player.account_id} className="matchInfo">
                                                    {player.level}
                                                </td>
                                                <td key={"key_" + player.account_id} className="matchInfo">
                                                    {player.kills}{" / "}{player.deaths}{" / "}{player.assists}
                                                </td>
                                                <td key={"key_" + player.account_id} className="matchInfo">
                                                    {player.gpm} {" / "} {player.xpm}
                                                </td>
                                                <td key={"key_" + player.account_id} className="matchInfo">
                                                    <ul>
                                                        <li>{player.item_0}{", "}{player.item_1}</li>
                                                        <li>{player.item_2}{", "}{player.item_3}</li>
                                                        <li>{player.item_4}{", "}{player.item_5}</li>
                                                    </ul>
                                                </td>
                                                                                        
                                                
                                            </tr>
                                        ) }})()} 
                                        </>
                                    )
                               
                            })}
                        </tbody>
                        </table>
                    

                    
                    <table className="MatchesTable">
                            <caption>Dire</caption>
                                    <thead>
                                        <tr>
                                        <th>Hero</th>
                                        <th>{/* Blank */}</th>
                                        <th>LVL</th>
                                        <th>K / D / A</th>
                                        <th>GPM / XPM</th>
                                        <th>Items</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                        {this.state.players.map(player => {
                            
                                    return (
                                        
                                        <>
                                        {(() => { if (player.player_slot > 120) {
                                            return (
                                        
                                            <tr key={player.id} className="gameInfoBox">
                                                <td key={"key_" + player.account_id} className="matchInfo">
                                                        
                                                    {this.state.heroes.map(hero => {
                                                        if (player.hero_id == hero.id) {
                                                            return (
                                                                <>
                                                                    <img key={"key_" + hero.id} src={hero.img}></img>
                                                                </>
                                                        )}
                                                    })}
                                                </td>
                                                <td key={"key_" + player.account_id} id={player.account_id} className="matchInfo">

                                                {(() => {
                                                    switch (player.account_id) {
                                                        case "private":
                                                            return <a id={player.account_id}>{player.personaname}</a>
                                                        default:
                                                            return <a href={"/player_" + player.account_id} id={player.account_id}>{player.personaname}</a>
                                                    }
                                                })()}
                                                    
                                                    
                                                </td>
                                                <td  className="matchInfo">
                                                    {player.level}
                                                </td>
                                                <td className="matchInfo">
                                                    {player.kills}{" / "}{player.deaths}{" / "}{player.assists}
                                                </td>
                                                <td key={"key_" + player.account_id} className="matchInfo">
                                                    {player.gpm} {" / "} {player.xpm}
                                                </td>
                                                <td  className="matchInfo">
                                                    <ul>
                                                        <li>{player.item_0}{", "}{player.item_1}</li>
                                                        <li>{player.item_2}{", "}{player.item_3}</li>
                                                        <li>{player.item_4}{", "}{player.item_5}</li>
                                                    </ul>
                                                </td>
                                                                                        
                                                
                                            </tr>
                                        ) }})()} 
                                        </>
                                    )
                               
                            })}
                        </tbody>
                        </table>
                    </div>

                    <div className="ChatLog"> 
                        <table className="MPTable">
                        <caption>Chat Log</caption>

                                <thead>
                                    <tr>
                                        <th>Player</th>
                                        <th></th>
                                        <th>Message</th>
                                        <th>Time</th>
                                    </tr>
                                </thead>
                                <tbody>
                        {
                        this.state.chats.map(chat => {
                            return (
                                <>   
                                    
                                    <tr key={"ChatLog"} className="peerInfoBox">
                                    
                                        <td key={"key_" + chat.timer} className="peerInfo">
                                        {this.state.players.map(player => {
                                            {this.state.heroes.map(hero => {
                                                if (player.player_slot == chat.player_slot) {
                                                        if (player.hero_id == hero.id) {
                                                            return (
                                                                <>
                                                                    <img key={"key_" + hero.id} src={hero.img}></img>
                                                                </>
                                                            )
                                                        }}
                                                })}


                                                   })}
                                            
                                        </td>  
                                        <td key={"key_2" + chat.timer} className="peerInfo" id={chat.type}>
                                            {this.state.players.map(player => {
                                                    if (chat.player_slot == player.player_slot) {
                                                        return (
                                                            <>
                                                                {player.personaname}
                                                            </>
                                                )}})}      
                                        </td>                
                                        <td key={"key_2" + chat.timer} className="peerInfo" id={chat.type}>
                                            {chat.message}
                                        </td>
                                        <td key={"key_2" + chat.timer} className="peerInfo" id={chat.type}>
                                            {chat.timer}
                                        </td>
                                       
                                    </tr>

                                    
                                    
                                </>
                            )//match return of the if inside map 
                        })}
                        </tbody>
                        </table>
                    </div>
                </>

            ) //match return in else of isLoading 

        } //match else of isLoading
    }


}
ReactDOM.render(<MyMatchDisplay />, document.querySelector('#divMatchDisplay'))

