import React, { Component } from 'react';



class App extends Component {
    state = {    };

    componentDidMount() {
        this.callApi()
            .then(res => this.setState({
               
            }))
            .catch(err => console.log(err));
    }

    callApi = async () => {
        const response = await fetch('url');
        const body = await response.json();
        if (response.status !== 200) throw Error(body.message);
        return body;
    };

    render() {

        return (
            <>

            </>

        )
    }
};

export default App;