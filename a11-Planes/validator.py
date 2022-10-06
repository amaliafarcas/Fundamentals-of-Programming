from exception import PlaneException


class ValidatePlane:
    def __init__(self):
        self.aux_plane_list = list()

    def validate_plane(self, row, col, orientation, plane_list):
        if orientation == 'N':
            if row < 1 or row > 7 or col < 3 or col > 8:
                raise PlaneException("Plane must fit the board")
            else:
                self.aux_plane_list = list()
                p = [row - 1, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col - 2]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col - 3]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col + 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row + 1, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row + 2, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row + 2, col - 2]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row + 2, col]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

        elif orientation == 'S':
            if row < 2 or row > 8 or col < 3 or col > 8:
                raise PlaneException("Plane must fit the board")
            else:
                self.aux_plane_list = list()
                p = [row + 1, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col + 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col - 2]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col - 3]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row - 1, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row - 2, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row - 2, col]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row - 2, col - 2]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

        elif orientation == 'E':
            if row < 2 or row > 7 or col < 3 or col > 9:
                raise PlaneException("Plane must fit the board")
            else:
                self.aux_plane_list = list()
                p = [row, col]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row + 1, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row + 2, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row - 1, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row - 2, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col - 2]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col - 3]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row + 1, col - 3]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row - 1, col - 3]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

        elif orientation == 'V':
            if row < 2 or row > 7 or col < 2 or col > 8:
                raise PlaneException("Plane must fit the board")
            else:
                self.aux_plane_list = list()
                p = [row, col - 2]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row - 1, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row - 2, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row + 1, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row + 2, col - 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row, col + 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row - 1, col + 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

                p = [row + 1, col + 1]
                if p not in plane_list:
                    self.aux_plane_list.append(p)
                else:
                    raise PlaneException("Planes must not overlap")

        else:
            raise PlaneException("Orientation must be N, E, S or V")

        return self.aux_plane_list
