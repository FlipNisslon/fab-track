
// Represents a single action in a process step, e.g., heating, exposure, etc.
export interface Step {
    id: string;
    name: string;
    description?: string;
    parameters: Record<string, any>; // e.g., { temperature: 200, pressure: 1.0 }
    durationMinutes?: number;
}
