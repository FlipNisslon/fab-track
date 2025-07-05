// Represents a group of steps within a process recipe
import { Step } from './step';

export interface ProcessStep {
    id: string;
    name: string;
    description?: string;
    steps: Step[];
}
