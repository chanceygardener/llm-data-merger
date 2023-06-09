import styles from './activeAggregation.module.css';
import { useState } from 'react';

const ActiveAggregation = ({ aggId, setActiveAggId }) => {

    const [activeAgg, setActiveAgg] = useState(null)

    const createAggregation = () => {
        console.log(`I run a create agg function`);
        setActiveAggId('TEST_AGG')
    }

    console.log(`Agg id is: ${JSON.stringify(aggId)}`)

    return aggId !== null ? (<div>
        <h1>I am an active aggregation</h1>
        <div>
            yup
        </div>
    </div>) : (<div>
        <p>Select an aggregation from the sidebar, or:</p>
        <button className={styles.Button} onClick={createAggregation}>
            Create one
        </button>
    </div>)
}


export default ActiveAggregation