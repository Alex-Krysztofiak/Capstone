class MySkillDisplay extends React.Component {
   constructor(props) {
      super(props)
      this.state = {
         skillIndex: 0,
         selectedIndices: [1, 2, 3],
         skills: [],
         isLoading: true,
         keyword: ""
      }
   }

   handleChange = e => {
      // I could change selctedIndices "directly" but it was not affecting the page
      // so I made a copy, changed the copy, and then used the copy to set the state
      let copy = this.state.selectedIndices;
      if (e.target.checked) {
         //remove from selectedIndices
         copy = copy.filter(function (element) {
            return element != e.target.value;
         });

      } else {
         //add to selectedIndices
         copy.push(e.target.value);
         copy.sort(function (a, b) { return a - b });
         //sort() assumes strings ("10"<"9") -- added anonymous "compare" function to force number (9<10)
      }

      this.setState({ selectedIndices: copy });
   }

   handleChange1 = e => {
      this.setState({ keyword: e.target.value });
      console.log(this.keyword)
      alert(this.keyword)
      document.getElementById("txt").value = this.keyword;
   }

   //note the JSON has a slightly different structure than before
   componentDidMount() {
      fetch('static\\JSON\\heroList.json')
         .then(response => response.json())
         .then(data => this.setState({ skills: data, isLoading: false }));
   }

   render() {
      if (this.state.isLoading) {
         return (<p>Loading ....</p>)
      } else {
         return (
            <>
               <span >
                  <ul>
                     <li>
                        <label>
                           <input type="checkbox" id="html1" name="agreement" value="1" onChange={this.handleChange} />
                           <img class="priAttrImg" src="static\\MiscImages\\hero_strength.png" />
                        </label>
                     </li>
                     <li>
                        <label>
                           <input type="checkbox" id="html" name="chooseAtt" value="2" onChange={this.handleChange} />
                           <img class="priAttrImg" src="static\\MiscImages\\hero_agility.png" />
                        </label>
                     </li>
                     <li>
                        <label>
                           <input type="checkbox" id="html" name="chooseAtt" value="3" onChange={this.handleChange} />
                           <img class="priAttrImg" src="static\\MiscImages\\hero_intelligence.png" />
                        </label>
                     </li>
                     <li>
                        <input
                           type="text"
                           id="txt1"
                           placeholder="Search here"
                           onChange={this.handleChange1}
                           value={this.state.keyword}
                        />
                     </li>
                     <li>
                        <input
                           type="text"
                           id="txt"
                           placeholder="Search here"
                           onChange={this.handleChange1}

                        />
                     </li>

                  </ul>


               </span>
               <br></br>
               {

                  this.state.skills.map((skill_element, i) => {
                     // if (document.getElementById("html1").isChecked() ){
                     //    alert("ok")
                     // }
                     for (let i = 0; i < this.state.selectedIndices.length; i++) {
                        if (this.state.selectedIndices[i] == 1 && skill_element.primary_attribute == "str") { //not found in selectedIndices array
                           //even though this is a map within a render it did not work with the single parent thing 
                           return (
                              <>

                                 <div name={"name_" + i} key={"key_" + i} className="flexChild" id={skill_element.primary_attribute}>
                                    <img name={"imgname_" + i} key={"imgkey_" + i} className="flexChildImg" src={skill_element.img}></img>
                                    <div name={"h1name_" + i} key={"h1key_" + i} className="flexChildInfo">
                                       <div name={"h1name_" + i} key={"h1key_" + i} className="flexChildInfo2">
                                          {/* {(() => {
                                                switch (skill_element.primary_attribute) {
                                                   case "str":   return <img className="priAttrImg" src={"static\\MiscImages\\hero_strength.png"}></img>;
                                                   case "agi": return <img className="priAttrImg" src={"static\\MiscImages\\hero_agility.png"}></img>;
                                                   case "int":  return <img className="priAttrImg" src={"static\\MiscImages\\hero_intelligence.png"}></img>;
                                                   default:      return "#FFFFFF";
                                                }
                                                })()} */}

                                       </div>

                                       <h1>{skill_element.name}</h1>



                                    </div>
                                    {/* <div name={"h1name_" + i} key={"h1key_" + i} className="flexChildInfo2">
                                                <h2>V</h2>
                                                <a href={skill_element.link} target="_blank"><h1>MORE INFO</h1></a>
                                             </div> */}
                                 </div>



                              </>
                           )//match return of the if inside map 
                        }//match if

                        if (this.state.selectedIndices[i] == 2 && skill_element.primary_attribute == "agi") { //not found in selectedIndices array
                           //even though this is a map within a render it did not work with the single parent thing 
                           return (
                              <>

                                 <div name={"name_" + i} key={"key_" + i} className="flexChild" id={skill_element.primary_attribute}>
                                    <img name={"imgname_" + i} key={"imgkey_" + i} className="flexChildImg" src={skill_element.img}></img>
                                    <div name={"h1name_" + i} key={"h1key_" + i} className="flexChildInfo">
                                       <div name={"h1name_" + i} key={"h1key_" + i} className="flexChildInfo2">
                                          {/* {(() => {
                                                switch (skill_element.primary_attribute) {
                                                   case "str":   return <img className="priAttrImg" src={"static\\MiscImages\\hero_strength.png"}></img>;
                                                   case "agi": return <img className="priAttrImg" src={"static\\MiscImages\\hero_agility.png"}></img>;
                                                   case "int":  return <img className="priAttrImg" src={"static\\MiscImages\\hero_intelligence.png"}></img>;
                                                   default:      return "#FFFFFF";
                                                }
                                                })()} */}

                                       </div>

                                       <h1>{skill_element.name}</h1>
                                       \


                                    </div>
                                    {/* <div name={"h1name_" + i} key={"h1key_" + i} className="flexChildInfo2">
                                                <h2>V</h2>
                                                <a href={skill_element.link} target="_blank"><h1>MORE INFO</h1></a>
                                             </div> */}
                                 </div>



                              </>
                           )//match return of the if inside map 
                        }//match if
                        if (this.state.selectedIndices[i] == 3 && skill_element.primary_attribute == "int") { //not found in selectedIndices array
                           //even though this is a map within a render it did not work with the single parent thing 
                           return (
                              <>

                                 <div name={"name_" + i} key={"key_" + i} className="flexChild" id={skill_element.primary_attribute}>
                                    <img name={"imgname_" + i} key={"imgkey_" + i} className="flexChildImg" src={skill_element.img}></img>
                                    <div name={"h1name_" + i} key={"h1key_" + i} className="flexChildInfo">
                                       <div name={"h1name_" + i} key={"h1key_" + i} className="flexChildInfo2">
                                          {/* {(() => {
                                                switch (skill_element.primary_attribute) {
                                                   case "str":   return <img className="priAttrImg" src={"static\\MiscImages\\hero_strength.png"}></img>;
                                                   case "agi": return <img className="priAttrImg" src={"static\\MiscImages\\hero_agility.png"}></img>;
                                                   case "int":  return <img className="priAttrImg" src={"static\\MiscImages\\hero_intelligence.png"}></img>;
                                                   default:      return "#FFFFFF";
                                                }
                                                })()} */}

                                       </div>

                                       <h1>{skill_element.name}</h1>



                                    </div>
                                    {/* <div name={"h1name_" + i} key={"h1key_" + i} className="flexChildInfo2">
                                                <h2>V</h2>
                                                <a href={skill_element.link} target="_blank"><h1>MORE INFO</h1></a>
                                             </div> */}
                                 </div>



                              </>
                           )//match return of the if inside map 
                        }//match if
                     }

                  }
                  )
               }
            </>
         ) //match return in else of isLoading 

      } //match else of isLoading
   }


}
ReactDOM.render(<MySkillDisplay />, document.querySelector('#divSkillDisplay'))
