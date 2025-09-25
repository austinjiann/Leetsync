class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # boxTypes[i] = [numBoxes, unitsPerBox]
        boxTypes.sort(key=lambda x: x[1], reverse=True)  # highest units first

        units = 0
        remaining = truckSize
        for count, per_box in boxTypes:
            if remaining == 0:
                break
            take = min(count, remaining)      # take as many as fit
            units += take * per_box           # add in one shot
            remaining -= take

        return units