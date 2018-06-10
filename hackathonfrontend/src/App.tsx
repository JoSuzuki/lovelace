import * as React from 'react';
import axios from 'axios';

class App extends React.Component <any, any> {
  public state={textFromServer: 'carregando'};
  
  public componentDidMount() {
    axios.get('http://127.0.0.1:8000/getjson/')
    .then(response => {
      console.log(response);
      this.setState({textFromServer: JSON.stringify(response)});
    })
    .catch(error => console.warn(error));
  }
  
  public render() {

    return (
      <React.Fragment>
        <div>{this.state.textFromServer}</div>
      </React.Fragment>
    );
  }

}

export default App;
