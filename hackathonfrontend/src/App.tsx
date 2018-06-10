import * as React from 'react';
import axios from 'axios';

class App extends React.Component <any, any> {
  public state={textFromServer: 'carregando'};
  
  public componentDidMount() {
    axios.get('https://lovelace.localtunnel.me/getjson/')
    .then(response => {
      console.log(response);
      this.setState({textFromServer: JSON.stringify(response.data)});
    })
    .catch(error => console.warn(error));
  }
  
  public render() {

    return (
      <React.Fragment>
        <div>{this.state.textFromServer}</div>
        <div>calma que</div>
      </React.Fragment>
    );
  }

}

export default App;
