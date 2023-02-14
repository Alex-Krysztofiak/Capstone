

class MySkillDisplay extends React.Component {
    constructor(props) {
       super(props)
       this.state = {
        skillIndex: 0,
        selectedIndices: [3, 4, 7],
        skills: [],
        isLoading: true,
        
       }
    }

    handleChange = e => {
        // I could change selctedIndices "directly" but it was not affecting the page
        // so I made a copy, changed the copy, and then used the copy to set the state
        let copy = this.state.selectedIndices;
        if (e.target.checked) {
           //add to selectedIndices
           copy.push(e.target.value);
           copy.sort(function (a, b) { return a - b });
           //sort() assumes strings ("10"<"9") -- added anonymous "compare" function to force number (9<10)
        } else {
           //remove from selectedIndices
           copy = copy.filter(function (element) {
              return element != e.target.value;
           });
        }
        this.setState({ selectedIndices: copy });
     }


    //note the JSON has a slightly different structure than before
    componentDidMount() {
        fetch('heroList.json')
           .then(response => response.json())
           .then(data => this.setState({ skills: data, isLoading: false }));
     }
    
     render() {
        if (this.state.isLoading) {
           return (<p>Loading ....</p>)
        } else {
            return (
                <>
                 
                   {
                      this.state.skills.map((skill_element, i) => {
                        if (this.state.selectedIndices.indexOf(i) == -1) { //not found in selectedIndices array
                            //even though this is a map within a render it did not work with the single parent thing 
                            return (
                               <>
                                     <div name={"name_" + skill_element} key={"3key_" + skill_element + skill_element.name} className="flexChild" >
                                        {skill_element.name}
                                     </div> 
                               </>
                            )//match return of the if inside map 
                         }//match if
                         else { //found in selectedIndices array  -- add "checked" property
                            return (
                               <>
                                  <div name={"name_" + skill_element} key={"key_" + skill_element + skill_element.name} className="flexChild" >
                                    {skill_element.name}
                                    </div> 
                               </>
                            ) //match return of the else inside map					
                         } //match else
                      }
                      )
                   }
                </>
             ) //match return in else of isLoading 
          
        } //match else of isLoading
     }
  

}
ReactDOM.render(<MySkillDisplay />, document.querySelector('#divSkillDisplay'))