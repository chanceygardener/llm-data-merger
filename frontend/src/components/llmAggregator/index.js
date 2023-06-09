import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import {
    Menu,
    MenuItem,
    Sidebar,
    // SidebarHeader,
    // SidebarFooter,
    // SidebarContent,
} from "react-pro-sidebar";
import ActiveAggregation from "./activeAggregation";

import styles from './llmAggregator.module.css';


const LlmAggregator = () => {

    const [sideBarCollapsed, setSideBarCollapsed] = useState(false);
    const [activeAggId, setActiveAggId] = useState(null);

    return (
        <div className={styles.console}>
            <div id="header" className={styles.Sidebar}>
                
                <Sidebar className={styles.app}>
                    <Menu>
                        <div className={styles.MenuHead}>
                            <bold>
                                Table Aggregations
                            </bold>
                        </div>
                        <MenuItem>
                            Heyooo
                        </MenuItem>
                        <MenuItem>
                            Holy Crackatoli
                        </MenuItem>
                    </Menu>
                </Sidebar>
                
            </div>
            <div className={styles.ActiveAgg} >
                <ActiveAggregation aggId={activeAggId} setActiveAggId={setActiveAggId} />
            </div>
        </div>)
}


export default LlmAggregator