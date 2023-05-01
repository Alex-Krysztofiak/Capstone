class MyBlogDisplay extends React.Component {
    constructor(props) {
       super(props)
       this.state = {
          newsIndex: 0,
          news: [],
          isLoading: true,
       }
    }


    //note the JSON has a slightly different structure than before
    componentDidMount() {
       fetch('static\\JSON\\patches.json')
          .then(response => response.json())
          .then(data => this.setState({ news: data, isLoading: false }));
    }
 
    render() {
        if (this.state.isLoading) {
            return (<p>Loading ....</p>)
        } else {
            return (
                
                <>
                    <div className="PlayerContainer"> 
                        
                        {this.state.news.map(news => {
                            return (
                                <>
                                    

                                    <div name={"name_"} key={"key_"} className="flexChild" id={news.name}>
                                        {/* <h2>{news.name}</h2> */}
                                        <a href={news.link} target="_blank"><img name={"imgname_"} key={"imgkey_"} className="flexChildImg" src={news.img}></img></a>
                                        
                                        <div name={"h1name_"} key={"h1key_"} className="flexChildInfo">
                                            <div name={"h1name_"} key={"h1key_"} className="flexChildInfo2"></div>
                                            <h1>{news.name}</h1>
                                        </div>
                                    </div>
                                        
                                </>
                            )
                        })}
                    </div>
               
                </>

            ) //match return in else of isLoading 

        } //match else of isLoading
    }
    
}

 ReactDOM.render(<MyBlogDisplay />, document.querySelector('#divBlogDisplay'))
 