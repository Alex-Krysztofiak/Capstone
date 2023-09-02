class MyMatchDisplay extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isLoading: true,
            players: [],
            items: []
        }
    }



    componentDidMount() {
        fetch('static\\JSON\\match_info.json')
            .then(response => response.json())
            .then(data => this.setState({ players: data, isLoading: false }));
        fetch('static\\JSON\\item_ids.json')
            .then(response => response.json())
            .then(data2 => this.setState({ items: data2, isLoading: false }));
        
    }

    render() {
        if (this.state.isLoading) {
            return (<p>Loading ....</p>)
        } else {
            return (
                <>
                    <div key="match" className="playerProfile">
                        {
                            this.state.players.map(player => {
                                return (
                                    <>
                                        <div key={"key_" + player.hero_id} className="gameInfoBox">
                                            <h1>
                                            
                                            {player.player_slot}{", "}
                                            {player.personaname}{", "}
                                            {player.account_id}{", "}
                                            {player.hero_id}{", "}
                                            {player.level}{", "}
                                            {player.item_0}{", "}
                                            {player.item_1}{", "}
                                            {player.item_2}{", "}
                                            {player.item_3}{", "}
                                            {player.item_4}{", "}
                                            {player.item_5}{", "}
                                            {player.gpm}{", "}
                                            </h1>
                                        </div>
                                    </>
                                )//match return of the if inside map 
                            })}
                    </div>
                </>

            ) //match return in else of isLoading 

        } //match else of isLoading
    }


}
ReactDOM.render(<MyMatchDisplay />, document.querySelector('#divMatchDisplay'))

