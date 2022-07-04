import React from 'react'
import { Card, Nav, Button } from 'react-bootstrap';

const Filter = ( props ) => {
  return (
    <Card>
        <Card.Body>
            <p>City</p>
            <p>Neighborhoods</p>
            <p>Price</p>
            
            <form>
                <input></input>
            </form>
            <Button variant="primary">Filter</Button>
        </Card.Body>
    </Card>
  )
}

export default Filter