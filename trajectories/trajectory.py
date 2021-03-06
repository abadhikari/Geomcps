class Trajectory:
    def __init__(self, pts):
        # self.pts = list(pts)
        self.pts = pts

    def resample(self, n):
        pass

    def __len__(self):
        return len(self.pts)

    def dim(self):
        return len(self.pts[0])

    def duration(self):
        return self.pts[-1].t - self.pts[0].t

    def __getitem__(self, item):
        return self.pts[item]

    def __iter__(self):
        return iter(self.pts)
